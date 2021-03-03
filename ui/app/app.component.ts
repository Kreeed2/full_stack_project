import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  url = 'http://static.218.251.203.116.clients.your-server.de:3333/'
  httpClient = null;
  public message$ = [];
  
  constructor(httpClient: HttpClient) {
    this.httpClient = httpClient;
    
    this.loadData();
  }
  
  loadData() {
      this.httpClient.get(this.url).toPromise().then(data => {
      var obj = JSON.parse(data.toString());
      console.log(obj);
      
      for (let key in obj){

        if (obj.hasOwnProperty(key)){
          this.message$.push(obj[key]);
        }
      }
      console.log(this.message$)
    });
  }
}
