import { Component, OnInit } from '@angular/core';
//import { Http } from '@angular/http';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(
  //  private http: Http
  ) { }

  ngOnInit() {
    /*this.http.get('http://127.0.0.1:8000/documents/', {search: {description: "COBRA", size: 30}}).subscribe(
      data => console.log(data.json()),
      err => console.error(err)
    );*/
  }

}
