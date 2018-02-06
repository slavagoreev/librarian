import { Component, Input, OnInit } from '@angular/core';
import { DocumentService } from '../../../core/services/document.service';

@Component({
  selector: 'app-document-item',
  templateUrl: './document-item.component.html',
  styleUrls: ['./document-item.component.scss']
})
export class DocumentItemComponent implements OnInit {
  @Input() document : Document;

  constructor(
    private documentService: DocumentService
  ) { }

  ngOnInit() {
  }
  deleteDocument(document_id: number){
    this.documentService.removeDocument(document_id).subscribe();
  }

}
