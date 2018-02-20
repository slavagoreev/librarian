import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
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
  documents: Document[];
  type = 'title';
  @ViewChild('searchInput')
  input: ElementRef;

  constructor(
    private documentService: DocumentService,
    private modalService: NgbModal
  ) {
    this.documentService.searchDocuments({size: 30}).subscribe(res => this.documents = res);
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
  search() {
    const options = { size: 30 },
          value = this.input.nativeElement.value;
    options[this.type] = value;
    console.log (options);
    this.documentService.searchDocuments(options).subscribe(res => {
      this.documents = res;
      this.highlight(value);
    });
  }
  selectType(type: string) {
    this.type = type;
  }
  highlight(text) {
    const results = document.getElementById("searchResults");
    const innerHTML = results.innerHTML;
    results.innerHTML = innerHTML.replace(text, `<span class="highlight">${text}</span>`);

}

}
