import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Store } from '@ngrx/store';
import { DocumentActions } from '../document/reducers/document.actions';
import { AppState } from '../interfaces';
import { getDocuments } from '../document/reducers/document.selectors';
import { DocumentService } from '../core/services/document.service';
import { Document } from '../shared/models/documents.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  documents$: Observable<Document[]>;

  constructor(
    private store: Store<AppState>,
    private actions: DocumentActions,
    private documentService: DocumentService
  ) {
    this.store.dispatch(this.actions.getAllDocuments());
    this.documents$ = this.store.select(getDocuments);
    console.log(this.documents$.subscribe(res => console.log (res)))
  }
  ngOnInit() {

  }
}
