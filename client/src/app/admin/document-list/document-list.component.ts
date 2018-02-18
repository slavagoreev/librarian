import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Document } from '../../shared/models/documents.model';
import { DocumentService } from '../../core/services/document.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-document-list',
  templateUrl: './document-list.component.html',
  styleUrls: ['./document-list.component.scss']
})
export class DocumentListComponent implements OnInit {
  documents$: Observable<Document[]>;
  constructor(
    private documentService: DocumentService,
    private modalService: NgbModal
  ) {
    this.documents$ = this.documentService.searchDocuments({size: 30});
  }

  ngOnInit() {
  }
  openModal(content, document: Document) {
    this.modalService.open(content).result.then((result: string) => {
      if (result == 'Confirm') {
        console.log ('Should be deleted', document);
      }
    });
  }

}
