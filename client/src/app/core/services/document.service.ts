import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import { HttpService } from './http.service';

@Injectable()
export class DocumentService {

  constructor(private http: HttpService) { }

  getDocument(id: string): Observable<any> {
    return this.http.get(`/document/${id}`)
      .map(res => res.json());
  }

  getDocuments(): Observable<any> {
    return this.http.get(`/documents/?size=10`)
      .map(res => res.json());
  }
}
