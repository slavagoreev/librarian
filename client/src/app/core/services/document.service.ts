import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import { HttpService } from './http.service';
import { Store } from '@ngrx/store';
import { AppState } from '../../interfaces';
import { DocumentActions } from '../../document/reducers/document.actions';
import { NotificationService } from '../../shared/components/notification/notification.service';
import * as _ from "lodash";
import { Document } from '../../shared/models/documents.model';
import { RequestOptions, URLSearchParams } from '@angular/http';

@Injectable()
export class DocumentService {

  constructor(
    private http: HttpService,
    private actions: DocumentActions,
    private store: Store<AppState>
  ) { }

  getDocument(id: number): Observable<Document> {
    return this.http.get(`documents/${id.toString()}`)
      .map(res => {
        const _res = res.json();
        console.log (_res.data)
        if (!_.isEmpty(_res.data)) {
          return _res.data as Document;
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Loading error',
              message: 'There is no document with this ID',
              delay: 20000
            }
          });
          return null;
        }
      });
  }

  getDocuments(): Observable<Document[]> {
    return this.http.get(`documents/?size=30&year=2018`)
      .map(res => {
        const _res = res.json();
        if (_res.data) {
          return _res.data
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Loading error',
              message: 'Could not load documents from server',
              delay: 20000
            }
          });
          return null;
        }
      });
  }
  searchDocuments(
    options: {
      title?: string,
      size?: number,
      offset?: number,
      author_name?: string,
      year?: number,
      tag_ids?: [number]
    }) : Observable<Document[]> {
    if (!options.size) options.size = 30;
    let str = "";
    for (let key in options) {
      if (str != "") str += "&";
      str += key + "=" + encodeURIComponent(options[key]);
    }
    return this.http.get(`documents/?${str}`)
      .map(res => {
        const _res = res.json();
        if (_res.data) {
          return _res.data
        } else {
          this.http.loading.next({
            loading: true,
            error: {
              title: 'Loading error',
              message: 'Could not load documents from server',
              delay: 20000
            }
          });
          return null;
        }
      });
  }
  removeDocument(id: number) {
    return this.http.delete(`documents/?id=${id.toString()}`)
      .map((res) => {
        return this.store.dispatch(this.actions.removeDocumentSuccess(id))
      });
  }
}
