import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import { HttpService } from './http.service';
import { Document } from '../../shared/models/documents.model';

@Injectable()
export class DocumentService {

  constructor(private http: HttpService) { }

  getDocument(id: string): Observable<Document> {
    return this.http.get(`/document/${id}`)
      .map(res => res.json());
  }

  getDocuments(): Observable<Document[]> {
    this.http.get(`/documents/`).subscribe(res => console.log(res));
    return this.http.get(`/documents/?size=10`)
      .map(res => res.json());
  }
}
