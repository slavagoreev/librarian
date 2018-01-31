import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'app';

  constructor(private http: HttpClient) {

  }
  ngOnInit(): void {
    this.http.get('http://127.0.0.1:8000/document/500').subscribe(data => {
      console.log(data);
    });
  }
}
