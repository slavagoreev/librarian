import { Component, Input, OnInit } from '@angular/core';
import {Document} from "../../shared/models/documents.model";

@Component({
  selector: 'app-document-list',
  templateUrl: './document-list.component.html',
  styleUrls: ['./document-list.component.scss']
})
export class DocumentListComponent implements OnInit {
  document: Document;
  @Input() documents;
  @Input() permission: boolean;

  constructor(){}

  ngOnInit() {

  }

}
