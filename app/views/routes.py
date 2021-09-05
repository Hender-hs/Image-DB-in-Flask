from app.modules.upload_files               import uploading_files, checking_extensions, getting_all_uploaded_files_in_folder, getting_request_files_names
from flask                                  import Flask, request, jsonify, send_from_directory
from app.modules                            import getting_all_uploaded_files
from app.modules                            import get_especific_file_to_download
from app.modules                            import ziping_files
from app.modules                            import type_upload_folder_list

def init_app(app: Flask, UPLOAD_FOLDER: str, ALLOWED_EXTENSIONS: str):

  @app.post('/upload')
  def upload_files():
  
    all_files_in_folder_set = getting_all_uploaded_files_in_folder(UPLOAD_FOLDER)

    request_files_names = getting_request_files_names(request.files)

    files_setlist_names = checking_extensions(request.files)


    if not files_setlist_names.issubset(ALLOWED_EXTENSIONS):
    
        return {'msg': 'extension is not allowed. allowed extensions .png, .jpg, gif'}, 415


    if all_files_in_folder_set.intersection(request_files_names) != set():
    
        return {'msg': 'already has this file on repository'}, 409


    try:
    
        uploaded_files = uploading_files(request.files, UPLOAD_FOLDER)

        return {'files_uploaded': uploaded_files}, 201

    except:
    
        return {'msg': 'some of your file is too large (size limit: 1MB)'}, 413
  
  
  
  @app.get('/files')
  def all_uploaded_files():
  
      files_all_files_list = getting_all_uploaded_files(UPLOAD_FOLDER) 
  
      return jsonify(files_all_files_list), 200
  
  
  
  @app.get('/files/<string:type>')
  def type_uploaded_files(type: str):
      
      files_type_list = type_upload_folder_list(type, UPLOAD_FOLDER)
      
      if files_type_list != 'there is no this file type':
      
          return jsonify(files_type_list), 200
  
      return {'msg': files_type_list}, 404
  
  
  
  @app.get('/download/<string:file_name>')
  def download_especifc_file(file_name: str):
      
      file_to_be_downloaded, file_path = get_especific_file_to_download(file_name, UPLOAD_FOLDER)
      
      if file_to_be_downloaded:
          
          return send_from_directory(f'{UPLOAD_FOLDER}/{file_path}', file_to_be_downloaded, as_attachment=True), 200
  
      return {'msg': 'file does not exists'}, 404
  
  
  @app.get('/download-zip')
  def download_zip_files():
      try:
      
          ziped_file_result = ziping_files(request.args, UPLOAD_FOLDER)
  
          if ziped_file_result == 'successful':
          
              return send_from_directory('/tmp/', 'all_files.zip', as_attachment=True), 200
  
          return {'msg': ziped_file_result}, 404
  
      except SyntaxError:
      
          return {'msg': 'must has these arguments as: file_type<string>, compression_rate<int>'}, 400

