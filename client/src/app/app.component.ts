import { Component, OnDestroy, OnInit } from '@angular/core';
import { ViewEncapsulation } from '@angular/compiler/src/core';
// import { Http, URLSearchParams } from '@angular/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  title = 'app';

  constructor() {

  }
  ngOnInit(): void {

  }
}
