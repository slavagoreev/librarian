import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DocumentActions } from '../../document/reducers/document.actions';
import { AppState } from '../../interfaces';
import { Store } from '@ngrx/store';
import { DocumentService } from '../../core/services/document.service';
import { UserService } from "../../core/services/user.service";

@Component({
  selector: 'app-bestseller-item',
  templateUrl: './bestseller-item.component.html',
  styleUrls: ['./bestseller-item.component.scss']
})
export class BestsellerItemComponent implements OnInit {
  @Input() document: Document;
  constructor(
    private documentService: DocumentService,
    private userService: UserService,
    private store: Store<AppState>,
    private actions: DocumentActions,
    private router: Router,
  ) {
  }

  ngOnInit() {
  }
  deleteDocument(document_id: number){
    this.documentService.removeDocument(document_id).subscribe();
  }
  selectDocument(document_id: number){
    this.store.dispatch(this.actions.getDocumentDetail(document_id));
    this.router.navigate(['/documents/', document_id.toString()])
  }
  bookDocument(documentId: number) {
    this.userService.bookTheDocument(documentId).subscribe(() => {
      this.router.navigate(['/user', 'orders'])
    });
  }

}
