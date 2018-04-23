import { Component, HostListener, Inject, Input, OnInit } from '@angular/core';
import { DOCUMENT } from '@angular/platform-browser';
import { WINDOW } from "../../../shared/services/scroll.service";
import { Document as DocumentModel } from '../../../shared/models/documents.model';
import { getUserRole } from '../../../auth/reducers/selectors';
import {UserService} from "../../../core/services/user.service";
import {Router} from "@angular/router";
import {DocumentService} from '../../../core/services/document.service';
import {AuthService} from "../../../core/services/auth.service";

@Component({
  selector: 'app-document-info',
  templateUrl: './document-info.component.html',
  styleUrls: ['./document-info.component.scss']
})
export class DocumentInfoComponent implements OnInit {
  @Input() document: DocumentModel;
  @Input() permission: boolean;
  thumbIsFixed: boolean;
  thumbWidth: number;
  description: string;
  tg_id: number;
  constructor(
    @Inject(DOCUMENT) private documentEl: Document,
    @Inject(WINDOW) private window,
    private userService: UserService,
    private authService: AuthService,
    private documentService: DocumentService,
    private router: Router,
  ) {
    this.userService.getUserData(this.authService.getUserData().id).subscribe(res => {
      this.tg_id = res.telegram_id;
    });
    if (this.tg_id === 0) {
      this.authService.telegramRegister().subscribe(res => {});
    }
  }

  bookDocument(documentId: number) {
    this.userService.bookTheDocument(documentId).subscribe(() => {
      this.router.navigate(['/user', 'orders']);
    });
  }

  outstandingRequest(documentId: number) {
    this.userService.outstandingRequest(documentId).subscribe(() => {
      this.documentService.getDocument(this.document.document_id).subscribe(data => {
        this.document = data;
      });
    });
  }

  ngOnInit() {
    console.log(this.tg_id);
    this.description = this.document.description.substr(0, 200);

  }
  extendDescription($event) {
    this.description = this.document.description;
    $event.target.style.setProperty('display', 'none');
  }

  addCopy(document: DocumentModel) {
    this.documentService.addCopy(document, 1, 'A').subscribe(res => {
      this.documentService.getDocument(this.document.document_id).subscribe(data => {
        this.document = data;
      });
    });
  }

  openTg() {
    window.open("https://oauth.telegram.org/auth?bot_id=566111170&origin=https%3A%2F%2Flibrarian.site&request_access=write",
      "", "width=550,height=450");
  }

  deleteCopy(id: number) {
    this.documentService.removeCopy(id).subscribe(res => {
      this.documentService.getDocument(this.document.document_id).subscribe(data => {
        this.document = data;
      });
    });
  }

  /*@HostListener("window:scroll", [])
  onWindowScroll() {
    let number = this.window.pageYOffset || this.documentEl.documentElement.scrollTop || this.documentEl.body.scrollTop || 0;
    if (number > 70 && this.description.length == this.document.description.length) {
      this.thumbIsFixed = true
    } else if (this.thumbIsFixed && number < 70) {
      this.thumbIsFixed = false;
    }
  }*/
}
