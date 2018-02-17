import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import { Effect, Actions } from '@ngrx/effects';

import { Action } from '@ngrx/store';
import { DocumentService } from '../../core/services/document.service';
import { DocumentActions } from './document.actions';
import { Document } from '../../shared/models/documents.model';


@Injectable()
export class DocumentEffects {
  constructor(private actions$: Actions,
              private documentService: DocumentService,
              private documentActions: DocumentActions) { }

  @Effect()
  GetAllDocuments$: Observable<Action> = this.actions$
    .ofType(DocumentActions.GET_ALL_DOCUMENTS)
    .switchMap((action: any) => this.documentService.getDocuments())
    .map((data: Document[]) => this.documentActions.getAllDocumentsSuccess(data));

  @Effect()
  GetDocumentDetail$: Observable<Action> = this.actions$
    .ofType(DocumentActions.GET_DOCUMENT_DETAIL)
    .switchMap((action: any) => this.documentService.getDocument(action.payload))
    .map((data: any) => this.documentActions.getDocumentDetailSuccess(data));
}
