import { Component, HostListener, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Store } from '@ngrx/store';
import { DocumentActions } from '../document/reducers/document.actions';
import { AppState } from '../interfaces';
import { getDocuments, getSelectedtDocument } from '../document/reducers/document.selectors';
import { DocumentService } from '../core/services/document.service';
import { Document } from '../shared/models/documents.model';
import { HttpService } from '../core/services/http.service';
import { LoaderComponent } from '../shared/components/loader/loader.component';
import { Subject } from 'rxjs/Subject';
import { getUserRole } from '../auth/reducers/selectors';
import { Router } from '@angular/router';
import {AuthService} from "../core/services/auth.service";
import {UserService} from "../core/services/user.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class HomeComponent implements OnInit, OnDestroy {
  innerWidth: number;
  documents$: Observable<Document[]>;
  loading$: Subject<{loading: boolean, error: any}>;
  // bestsellers$: Observable<Document[]>;
  bestsellers$: Document[];
  currentPage: number = 0;
  scrollCallback: any;
  permission: boolean;
  allowToLoadCallback;

  constructor(
    private store: Store<AppState>,
    private actions: DocumentActions,
    private http: HttpService,
    private router: Router,
    private documentService: DocumentService,
    private authService: AuthService,
    private userService: UserService
  ) {
    this.store.select(getUserRole).subscribe(res => this.permission = (res == 310 || res == 320 || res == 330));
    this.loading$ = this.http.loading;
    this.innerWidth = window.innerWidth;
    this.scrollCallback = this.getDocuments.bind(this);
    this.documents$ = this.store.select(getDocuments)
      .map(res => { res.map(doc => doc as Document); return res})
      .do(this.processData);
    this.getDocuments(() => {});
  }
  getDocuments(cb) {
    // console.error ('should load')
    this.store.dispatch(this.actions.getDocumentsWithOffset({ offset: this.currentPage * 30}));
    this.allowToLoadCallback = cb;
  }
  private processData = (data) => {
    // onsole.error ("proceed", data);
    this.currentPage++;
    this.allowToLoadCallback();
  };

  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.innerWidth = window.innerWidth;
  }
  ngOnInit() {
    this.documentService.getBestsellers().subscribe(res => {
      this.bestsellers$ = res;
    });

  }
  sleep(milliseconds) {
    let start = new Date().getTime();
    for (let i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds){
        break;
      }
    }
  }
  selectDocument(document_id: number){
    this.store.dispatch(this.actions.getDocumentDetail(document_id));
    this.router.navigate(['/documents/', document_id.toString()])
  }
  ngOnDestroy() {
    this.store.dispatch(this.actions.clearDocuments());
  }
}
