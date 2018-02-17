import { Component, Input, OnInit } from '@angular/core';
import { DocumentService } from '../../../core/services/document.service';
import { Store } from '@ngrx/store';
import { AppState } from '../../../interfaces';
import { DocumentActions } from '../../../document/reducers/document.actions';

@Component({
  selector: 'app-document-item',
  templateUrl: './document-item.component.html',
  styleUrls: ['./document-item.component.scss']
})
export class DocumentItemComponent implements OnInit {
  @Input() document : Document;

  constructor(
    private documentService: DocumentService,
    private store: Store<AppState>,
    private actions: DocumentActions,
  ) { }

  ngOnInit() {
  }
  deleteDocument(document_id: number){
    this.documentService.removeDocument(document_id).subscribe();
  }
  selectDocument(document_id: number){
    this.store.dispatch(this.actions.getDocumentDetail(document_id));
  }

}
