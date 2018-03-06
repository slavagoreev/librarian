import { Pipe, PipeTransform } from '@angular/core';

@Pipe({name: 'documentType'})
export class DocumentTypePipe implements PipeTransform {
  transform(value: number): string {
    switch (value) {
      case 0: return "Book";
      case 1: return "Journal Article";
      case 2: return "Audio / Video file";
    }
  }
}

@Pipe({name: 'documentTypeClass'})
export class DocumentTypeClassPipe implements PipeTransform {
  transform(value: number): string {
    switch (value) {
      case 0: return "book";
      case 1: return "journal";
      case 2: return "av";
    }
  }
}
