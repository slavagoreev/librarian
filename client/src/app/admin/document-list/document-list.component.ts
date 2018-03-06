import { Component, ElementRef, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { Observable, Subscribable } from 'rxjs/Observable';
import { Document } from '../../shared/models/documents.model';
import { DocumentService } from '../../core/services/document.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { Subscription } from 'rxjs/Subscription';

@Component({
  selector: 'app-document-list',
  templateUrl: './document-list.component.html',
  styleUrls: [ './document-list.component.scss' ]
})
export class DocumentListComponent implements OnInit, OnDestroy {
  documents: Document[] = [];
  type = 'title';
  options: {
    size: number,
    offset: number,
    type?: string
  } = { size: 30, offset: 0 };
  @ViewChild('searchInput')
  input: ElementRef;
  currentPage: number = 0;
  scrollCallback: any;
  loading: boolean = false;
  subscription: Subscription;

  constructor(private documentService: DocumentService,
              private activatedRoute: ActivatedRoute,
              private modalService: NgbModal) {
    this.scrollCallback = this.getDocuments.bind(this);
    this.getDocuments();
  }

  getDocuments(cb = () => {}) {
    if (!this.loading) {
      console.error('should load', this.options);
      this.subscription = this.documentService.searchDocuments(this.options)
        .subscribe(data => this.processData(data))
    }
  }

  private processData = (data) => {
    console.error("proceed");
    this.documents = this.documents.concat(data);
    this.loading = false;
    this.currentPage++;
    this.options.offset = this.options.size * this.currentPage;
  };

  ngOnInit() {
  }

  openModal(content, document: Document) {
    this.modalService.open(content).result.then((result: string) => {
      if (result == 'Confirm') {
        console.log('Should be deleted', document);
      }
    });
  }

  search() {
    const value = this.input.nativeElement.value;
    console.error(this.input.nativeElement.value);
    this.options[this.type] = value;
    this.getDocuments()
  }

  selectType(type: string) {
    this.type = type;
  }

  highlight(text) {
    const results = document.getElementById("searchResults");
    const innerHTML = results.innerHTML;
    results.innerHTML = innerHTML.replace(text, `<span class="highlight">${text}</span>`);
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}
