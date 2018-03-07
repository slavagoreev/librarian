import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DocumentActions } from '../../document/reducers/document.actions';
import { AppState } from '../../interfaces';
import { Store } from '@ngrx/store';

@Component({
  selector: 'app-bestseller-item',
  templateUrl: './bestseller-item.component.html',
  styleUrls: ['./bestseller-item.component.scss']
})
export class BestsellerItemComponent implements OnInit {
  @Input() document: Document;
  @Input() width: number;
  constructor(
    private store: Store<AppState>,
    private actions: DocumentActions,
    private router: Router,
  ) {
  }

  ngOnInit() {
  }
  selectDocument(document_id: number){
    console.log (document_id);
    this.store.dispatch(this.actions.getDocumentDetail(document_id));
    this.router.navigate(['/documents/', document_id.toString()])
  }

}
