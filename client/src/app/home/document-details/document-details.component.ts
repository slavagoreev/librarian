import { Component, HostListener, OnDestroy, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { DocumentService } from '../../core/services/document.service';
import { ActivatedRoute } from "@angular/router";
import { Subscription } from 'rxjs/Subscription';
import { Document } from '../../shared/models/documents.model';
import { getUserRole } from '../../auth/reducers/selectors';
import { AppState } from '../../interfaces';
import { Store } from '@ngrx/store';

@Component({
  selector: 'app-document-details',
  templateUrl: './document-details.component.html',
  styleUrls: ['./document-details.component.scss']
})
export class DocumentDetailsComponent implements OnInit, OnDestroy {
  innerHeight: number;
  documentId: any;
  actionsSubscription: Subscription;
  document: Document;
  permission: boolean;

  constructor(
    private store: Store<AppState>,
    private documentService: DocumentService,
    private router : ActivatedRoute
  ) {
    this.actionsSubscription = this.router.params.subscribe((params: any) => {
      this.documentId = params['id'];
      this.documentService
        .getDocument(this.documentId)
        .subscribe(res => {
          this.document = res
        });
    });
    this.store.select(getUserRole).subscribe(res => this.permission = res == 2);
    this.innerHeight =window.innerHeight;
  }
  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.innerHeight = window.innerHeight;
  }
  ngOnInit() {
  }

  ngOnDestroy() {
    this.actionsSubscription.unsubscribe();
  }
}
