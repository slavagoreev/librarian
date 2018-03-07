import { AfterViewInit, Directive, ElementRef, Input } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/fromEvent';
import 'rxjs/add/operator/pairwise';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/exhaustMap';
import 'rxjs/add/operator/filter';
import 'rxjs/add/operator/startWith';
import 'rxjs/add/operator/distinctUntilKeyChanged';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/distinct';

interface ScrollPosition {
  sH: number;
  sT: number;
  cH: number;
};

const DEFAULT_SCROLL_POSITION: ScrollPosition = {
  sH: 0,
  sT: 0,
  cH: 0
};

@Directive({
  selector: '[appInfiniteScroller]'
})
export class InfiniteScrollerDirective implements AfterViewInit {

  private scrollEvent$;

  private userScrolledDown$;

  private loadingIsDone: boolean = true;

  @Input()
  scrollCallback;

  @Input()
  immediateCallback;

  @Input()
  scrollPercent = 80;

  constructor(private elm: ElementRef) {
  }

  ngAfterViewInit() {

    this.registerScrollEvent();

    this.streamScrollEvents();

    this.requestCallbackOnScroll();

  }

  private registerScrollEvent() {
    this.scrollEvent$ = Observable.fromEvent(window, 'scroll');
  }

  private streamScrollEvents() {
    this.userScrolledDown$ = this.scrollEvent$
      .map((e: any): ScrollPosition => ({
        sH: e.target.scrollingElement.scrollHeight,
        sT: e.target.scrollingElement.scrollTop,
        cH: e.target.scrollingElement.clientHeight
      }))
      .pairwise()
      .filter(positions => (
        this.isUserScrollingDown(positions) &&
        this.isScrollExpectedPercent(positions[1]) &&
        this.loadingIsDone));
  }

  private requestCallbackOnScroll() {
    this.userScrolledDown$
      .subscribe(() => {
        this.loadingIsDone = false;
        return this.scrollCallback(() => {
          this.loadingIsDone = true;
        });
      });

  }

  private isUserScrollingDown = (positions) => {
    return positions[0].sT < positions[1].sT;
  }

  private isScrollExpectedPercent = (position) => {
    return ((position.sT + position.cH) / position.sH) > (this.scrollPercent / 100);
  }

}
