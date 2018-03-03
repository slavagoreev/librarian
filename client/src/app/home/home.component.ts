import { Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
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

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class HomeComponent implements OnInit, OnDestroy {

  documents$: Observable<Document[]>;
  loading$: Subject<{loading: boolean, error: any}>;
  // bestsellers$: Observable<Document[]>;
  bestsellers$: Document[];
  permission: boolean;

  constructor(
    private store: Store<AppState>,
    private actions: DocumentActions,
    private http: HttpService,
    private documentService: DocumentService
  ) {
    this.store.dispatch(this.actions.getAllDocuments());
    this.store.select(getUserRole).subscribe(res => this.permission = res == 2);
    this.documents$ = this.store.select(getDocuments)
      .map(res => { res.map(doc => doc as Document); return res});

    this.loading$ = this.http.loading;
  }

  ngOnInit() {
    this.documents$.subscribe(res => {
      this.bestsellers$ = res;
    });
  }
  ngOnDestroy() {
  }
}
