import { Component, OnInit } from '@angular/core';
import { FileUploadService } from '../file-upload.service'

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.scss']
})
export class FileUploadComponent implements OnInit {

  fileToUpload: File = null;
  fileUploadService = null;

  constructor(fileUploadService: FileUploadService) { 
    this.fileUploadService = fileUploadService;
  }

  ngOnInit(): void {
  }
  
  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }
  
  uploadFileToActivity() {
    this.fileUploadService.postFile(this.fileToUpload).subscribe(data => {
       console.log("File send");
       window.location.reload();
      }, error => {
        console.log(error);
      });
  }

}
