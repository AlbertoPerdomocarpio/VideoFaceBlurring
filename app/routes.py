import os
from flask import Blueprint, abort, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from app.utils import censor_faces

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('video')
        if not file:
            return "No file uploaded", 400

        filename = secure_filename(file.filename)
        input_path = os.path.join('app/uploads', filename)
        file.save(input_path)

        output_filename = f"censored_{filename}"
        output_path = os.path.join('app/processed', output_filename)
        censor_faces(input_path, output_path)

        return redirect(url_for('main.download', filename=output_filename))

    return render_template('index.html')

@bp.route('/download/<filename>')
def download(filename):
    file_path = os.path.abspath(os.path.join('app/processed', filename))

    if not os.path.exists(file_path):
        abort(404, description="File not found")

    return send_file(file_path, as_attachment=True)




@bp.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return "No video file provided", 400

    video = request.files['video']
    input_path = os.path.join('app/uploads', video.filename)
    output_filename = f"processed_{video.filename}"
    output_path = os.path.join('app/processed', output_filename)

    video.save(input_path)

    censor_faces(input_path, output_path)

    os.remove(input_path)

    return {"processed_file": output_filename}, 200

