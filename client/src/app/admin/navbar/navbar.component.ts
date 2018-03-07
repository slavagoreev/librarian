import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  permission: boolean;
  constructor(
    private router: Router
  ) { }

  ngOnInit() {
    console.log (this.router.url)
    this.permission = this.router.url.search('librarian') > -1
  }

}
