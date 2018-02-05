import { Component, OnDestroy, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Store } from '@ngrx/store';
import { DocumentActions } from '../document/reducers/document.actions';
import { AppState } from '../interfaces';
import { getDocuments, getSelectedtDocument } from '../document/reducers/document.selectors';
import { DocumentService } from '../core/services/document.service';
import { Document } from '../shared/models/documents.model';
import { log } from 'util';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit, OnDestroy {

  documents$: Observable<Document[]>;

  constructor(
    private store: Store<AppState>,
    private actions: DocumentActions,
    private documentService: DocumentService
  ) {
    this.store.dispatch(this.actions.getAllDocuments());
    this.documents$ = this.store.select(getDocuments)
      .map(res => { res.map(doc => doc as Document); console.log (res);return res});

    console.log (this.store.select(getDocuments))
  }
  ngOnInit() {

  }
  ngOnDestroy() {
  }
}
