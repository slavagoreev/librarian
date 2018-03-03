import { Component, HostListener, OnDestroy, OnInit } from '@angular/core';
import { ViewEncapsulation } from '@angular/compiler/src/core';
// import { Http, URLSearchParams } from '@angular/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  title = 'app';
  imageShow = false;

  constructor() {

  }
  ngOnInit(): void {

  }
  @HostListener('document:keypress', ['$event'])
  handleKeyboardEvent($event: KeyboardEvent) {
    if ($event.ctrlKey && $event.key.toLocaleLowerCase() === 't') {
      this.imageShow = !this.imageShow;
    }
  }
}
