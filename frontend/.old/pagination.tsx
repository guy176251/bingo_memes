import { FunctionComponent } from 'react';

interface PageElemProps {
  index: number;
}
type PageElemType = FunctionComponent<PageElemProps>;

interface PaginationItemsProps {
  pageNum: number;
  pages: number;
  PageElem: PageElemType;
  PageEllipseElem: PageElemType;
}

const PaginationItems = ({ pageNum, pages, PageElem, PageEllipseElem }: PaginationItemsProps) => {
  var current = pageNum,
      last = pages,
      delta = 2,
      left = current - delta,
      right = current + delta + 1,
      range = [],
      rangeWithDots = [],
      l;

  for (let i = 1; i <= last; i++) {
    if (i == 1 || i == last || i >= left && i < right) {
      range.push(i);
    }
  }

  for (let i of range) {
    if (l) {
      if (i - l === 2) {
        rangeWithDots.push(<PageElem index={l +1}/>);
      } else if (i - l !== 1) {
        rangeWithDots.push(<Pagination.Ellipsis disabled />);
      }
    }
    rangeWithDots.push(pageItem(i));
    l = i;
  }

  return rangeWithDots;
};

export default paginationItems;
