import { Pipe, PipeTransform } from '@angular/core';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

@Pipe({name: 'userRole'})
export class UserRolePipe implements PipeTransform {
  constructor(private sanitizer: DomSanitizer){

  }
  transform(value: number): SafeHtml {
    switch (value) {
      case 0: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-secondary">Patron</span>`);
      case 1: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-success">Faculty</span>`);
      case 2: return this.sanitizer.bypassSecurityTrustHtml(`<span class="badge badge-warning">Librarian</span>`);
    }
  }
}

@Pipe({name: 'plainUserRole'})
export class PlainUserRolePipe implements PipeTransform {
  constructor(private sanitizer: DomSanitizer){

  }
  transform(value: number): string {
    switch (value) {
      case 0: return "Student";
      case 1: return "Faculty";
      case 2: return "Librarian";
    }
  }
}
