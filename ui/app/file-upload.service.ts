import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class FileUploadService {
  
  httpClient = null;
  
  constructor(httpClient: HttpClient) {
    this.httpClient = httpClient;
  }
  
  postFile(fileToUpload: File): Observable<boolean> {
    const endpoint = 'http://static.218.251.203.116.clients.your-server.de:3333/fileUpload';
    const formData: FormData = new FormData();
    formData.append('data', fileToUpload, fileToUpload.name);
    return this.httpClient
      .post(endpoint, formData, { });
      // .map(() => { return true; })
      // .catch((e) => this.handleError(e));
  }
  
  handleError(e) {
    console.log(e);
  }
}
