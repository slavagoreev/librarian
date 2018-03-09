import { Component, ElementRef, HostListener, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { User } from '../../../shared/models/users.model';
import { Subscription } from 'rxjs/Subscription';
import { UserService } from '../../../core/services/user.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../../core/services/auth.service';
import {until} from 'selenium-webdriver';
import titleContains = until.titleContains;
import {Document} from '../../../shared/models/documents.model';
import {DocumentService} from '../../../core/services/document.service';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.scss']
})
export class AddComponent implements OnInit {

  subscription: Subscription;
  userChangeSubscription: Subscription;
  // document: Document;
  document = new Document;
  @ViewChild('addTitle')
  title: ElementRef;
  @ViewChild('addPublisher')
  publisher: ElementRef;
  @ViewChild('addAuthors')
  authors: ElementRef;
  @ViewChild('addYear')
  year: ElementRef;
  @ViewChild('addDescription')
  description: ElementRef;
  @ViewChild('addCover')
  cover: ElementRef;
  @ViewChild('addDocumentType')
  document_type: ElementRef;
  @ViewChild('addPrice')
  price: ElementRef;
  @ViewChild('addReference')
  is_reference: ElementRef;
  @ViewChild('addBestseller')
  is_bestseller: ElementRef;

  userEditInfoForm: FormGroup;

  private innerHeight: number;
  private userId: number;
  constructor(
    private fb: FormBuilder,
    private documentService: DocumentService,
    private authService: AuthService,
    private router: ActivatedRoute,
    private linker: Router
  ) {
    this.subscription = this.router.params.subscribe((params: any) => {
      this.userId = params['id'] || authService.getUserData().id;
    });
    this.innerHeight = window.innerHeight;
  }
  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.innerHeight = window.innerHeight;
  }
  ngOnInit() {
    this.document.is_reference = false;
    this.document.is_bestseller = false;
    this.initUserEditForm();
  }
  initUserEditForm() {
    const authors = '',
      publisher = '', is_reference = 0, is_bestseller = 0,
      price = '', year = '', cover = '',
      description = '', document_type = 0,
      title = '';
    this.userEditInfoForm = this.fb.group({
        'title': [title, Validators.required],
        'publisher': [publisher, Validators.required],
        'authors': [authors, Validators.required],
        'year': [year, Validators.required],
        'description': [description],
        'cover': [cover],
        'document_type': [document_type, Validators.required],
        'price': [price, Validators.required],
        'is_reference': [is_reference],
        'is_bestseller': [is_bestseller],
      }
    );
  }

  onReferenceChange() {
    this.document.is_reference = !this.document.is_reference;
  }

  onBestsellerChange() {
    this.document.is_bestseller = !this.document.is_bestseller;
  }

  onSubmit() {
    const values = this.userEditInfoForm.value;
    const keys = Object.keys(values);
    if (this.userEditInfoForm.valid) {
      console.log (this.userEditInfoForm);
      /*this.userChangeSubscription = this.authService.register(values).subscribe(data => {
        const errors = data;
        console.log (data);
        if (errors) {
          keys.forEach(val => {
            if (errors[val]) { this.pushErrorFor(val, errors[val][0]); };
          });
        }
      });*/
    } else {
      keys.forEach(val => {
        const ctrl = this.userEditInfoForm.controls[val];
        if (!ctrl.valid) {
          this.pushErrorFor(val, null);
          ctrl.markAsTouched();
        };
      });
    }
  }

  submitForm() {
    this.document.title = this.title.nativeElement.value;
    this.document.publisher = this.publisher.nativeElement.value;
    this.document.authors = this.authors.nativeElement.value;
    this.document.year = this.year.nativeElement.value;
    this.document.description = this.description.nativeElement.value;
    this.document.cover = this.cover.nativeElement.value;
    this.document.document_type = this.document_type.nativeElement.value;
    this.document.price = this.price.nativeElement.value;
    this.document.copies_available = 0;
    this.document.tags = [];
    this.documentService.addDocument(this.document).subscribe(res => {
      this.linker.navigate(['librarian/document-list/']);
    });
  }

  private pushErrorFor(ctrl_name: string, msg: string) {
    console.log (ctrl_name, msg);
    if (this.userEditInfoForm.controls[ctrl_name])
      this.userEditInfoForm.controls[ctrl_name].setErrors({'msg': msg});
    else this.userEditInfoForm.controls[ctrl_name].setErrors({'msg': msg});
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
    if (this.userChangeSubscription) {
      this.userChangeSubscription.unsubscribe();
    }
  }

}
