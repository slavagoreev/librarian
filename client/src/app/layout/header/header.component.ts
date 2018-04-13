import { Component, HostListener, Inject, OnInit } from '@angular/core';
import { DOCUMENT } from '@angular/platform-browser';
import { WINDOW } from "../../shared/services/scroll.service";
import { AuthState } from '../../auth/reducers/auth.state';
import { Store } from '@ngrx/store';
import { AppState } from '../../interfaces';
import { getAuthStatus, getUserRole } from '../../auth/reducers/selectors';
import { Observable } from 'rxjs/Observable';
import { AuthActions } from "../../auth/actions/auth.actions";
import { AuthService } from '../../core/services/auth.service';
import { User } from '../../shared/models/users.model';
import {DocumentService} from '../../core/services/document.service';
import {Document as Doc} from '../../shared/models/documents.model';
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
  user$: User;
  documents$: Observable<Doc[]>;
  isAdmin: boolean;

  constructor(
    @Inject(DOCUMENT) private document: Document,
    @Inject(WINDOW) private window,
    private authActions: AuthActions,
    private authService: AuthService,
    private store: Store<AppState>,
    private documentService: DocumentService
  ) {
    this.store.dispatch(this.authActions.authorize());
    this.store.select(getAuthStatus).subscribe((auth) => {
      this.isAuthenticated = auth;
      if (auth) {
        this.user$ = this.authService.getUserData()
      }
    });
    this.store.select(getUserRole).subscribe((role) => {
      this.isAdmin = (role === 310 || role === 320 || role === 330);
    });
  }

  ngOnInit() {
    if (this.isAuthenticated) {
      this.documentService.getDocuments().subscribe(res => {
        this.documents$ = Observable.of(res);
      });
    }
  }
  setSearchState(state: boolean) {
    this.searchOpen = state;
  }
  logout() {
    this.authService.logout().subscribe(() => {})
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
