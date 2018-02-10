import { Component, HostListener, Inject, OnInit } from '@angular/core';
import { DOCUMENT } from '@angular/platform-browser';
import { WINDOW } from "../../shared/services/scroll.service";
import { AuthState } from '../../auth/reducers/auth.state';
import { Store } from '@ngrx/store';
import { AppState } from '../../interfaces';
import { getAuthStatus } from '../../auth/reducers/selectors';
import { Observable } from 'rxjs/Observable';
import { AuthActions } from "../../auth/actions/auth.actions";
//import { Http } from '@angular/http';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  public navIsFixed: boolean = false;
  searchOpen: boolean = false;
  isAuthenticated: boolean;

  constructor(
    @Inject(DOCUMENT) private document: Document,
    @Inject(WINDOW) private window,
    private authActions: AuthActions,
    private store: Store<AppState>
  ) {
    this.store.dispatch(this.authActions.authorize());
    this.store.select(getAuthStatus).subscribe((auth) => {
      console.log (auth);
      this.isAuthenticated = auth;
    });
  }

  ngOnInit() {

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
