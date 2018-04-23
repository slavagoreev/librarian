import { Pipe, PipeTransform } from '@angular/core';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

@Pipe({name: 'userRole'})
export class UserRolePipe implements PipeTransform {
  constructor(private sanitizer: DomSanitizer){

  }
  transform(value: number): SafeHtml {
    switch (value) {
      case 100: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-secondary">Patron</span>`);
      case 210: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-success">Instructor</span>`);
      case 220: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-success">Teacher Assistant</span>`);
      case 230: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-success">Visiting Professor</span>`);
      case 240: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-success">Professor</span>`);
      case 310: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-warning">Librarian 1</span>`);
      case 320: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-warning">Librarian 2</span>`);
      case 330: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-warning">Librarian 3</span>`);
    }
  }
}

@Pipe({name: 'plainUserRole'})
export class PlainUserRolePipe implements PipeTransform {
  constructor(private sanitizer: DomSanitizer){

  }
  transform(value: number): string {
    switch (value) {
      case 100: return "Student";
      case 210: return "Instructor";
      case 220: return "Teacher Assistant";
      case 230: return "Visiting Professor";
      case 240: return "Professor";
      case 310: return "Librarian 1";
      case 320: return "Librarian 2";
      case 330: return "Librarian 3";
    }
  }
}
