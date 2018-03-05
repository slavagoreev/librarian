import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Document } from '../../shared/models/documents.model';
import { DocumentService } from '../../core/services/document.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-document-list',
  templateUrl: './document-list.component.html',
  styleUrls: ['./document-list.component.scss']
})
export class DocumentListComponent implements OnInit {
  documents$: Observable<Document[]>;
  type = 'title';
  @ViewChild('searchInput')
  input: ElementRef;

  constructor(
    private documentService: DocumentService,
    private activatedRoute: ActivatedRoute,
    private modalService: NgbModal
  ) {
    let options = { size: 30 };
    this.activatedRoute.queryParamMap.subscribe(params => {
      console.log (params)
      this.documents$ = this.documentService.searchDocuments(options);
    });
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
    console.error(this.input.nativeElement.value);
    options[this.type] = value;
    this.documents$ = this.documentService.searchDocuments(options);
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
