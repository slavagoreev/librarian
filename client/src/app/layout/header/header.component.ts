import { Component, HostListener, Inject, OnInit } from '@angular/core';
import { DOCUMENT } from '@angular/platform-browser';
import { WINDOW } from "../../shared/services/scroll.service";
//import { Http } from '@angular/http';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  public navIsFixed: boolean = false;
  searchOpen: boolean = false;

  constructor(
    @Inject(DOCUMENT) private document: Document,
    @Inject(WINDOW) private window
  ) { }

  ngOnInit() {
    /*this.http.get('http://127.0.0.1:8000/documents/', {search: {description: "COBRA", size: 30}}).subscribe(
      data => console.log(data.json()),
      err => console.error(err)
    );*/
  }
  setSearchState(state: boolean) {
    this.searchOpen = state;
  }
  @HostListener("window:scroll", [])
  onWindowScroll() {
    let number = this.window.pageYOffset || this.document.documentElement.scrollTop || this.document.body.scrollTop || 0;
    if (number > 250) {
      this.navIsFixed = true;
    } else if (this.navIsFixed && number < 10) {
      this.navIsFixed = false;
    }
  }

}
