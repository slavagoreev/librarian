import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import { HttpService } from './http.service';
import { Store } from '@ngrx/store';
import { AppState } from '../../interfaces';
import { DocumentActions } from '../../document/reducers/document.actions';

@Injectable()
export class DocumentService {

  constructor(
    private http: HttpService,
    private actions: DocumentActions,
    private store: Store<AppState>
  ) { }

  getDocument(id: number): Observable<any> {
    return this.http.get(`document/${id.toString()}`)
      .map(res => res.json());
  }

  getDocuments(): Observable<any> {
    return this.http.get(`documents/?size=30&title=Computer+Science`)
      .map(res => {
        const data = res.json();
        console.log (data);
        return data
      });
  }
  removeDocument(id: number) {
    return this.http.delete(`documents/?id=${id.toString()}`)
      .map((res) => {
        return this.store.dispatch(this.actions.removeDocumentSuccess(id))
      });
  }
}
