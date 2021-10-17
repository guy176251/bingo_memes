import React, { useState, useEffect } from 'react';

import Spinner from 'react-bootstrap/Spinner';
//import Button from 'react-bootstrap/Button';
import Pagination from 'react-bootstrap/Pagination';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Dropdown from 'react-bootstrap/Dropdown';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

import { BingoCard, ViewProps } from './types';
import CardInfo from './cardinfo';
import { AppNavBar } from './navbar';
import apiCall from './apicaller';

interface BingoCardPage {
  detail?: string;
  count: number;
  next: string | null;
  previous: string | null;
  results: Array<BingoCard>;
}

type CardPage = BingoCardPage | null;

var searchInput = '';
var searchQuery = '';
var orderedBy = '';
var orderedByLabel = 'Sort';
var pageNum = 1;
var loaded = false;
const resultsLen = 10;

interface SearchBarProps {
  beginLoad: () => void;
}

const SearchBar = ({ beginLoad }: SearchBarProps) => {
  //const [sortDisplayLabel, setSortDisplayLabel] = useState(searchQuery ? searchQuery : 'Sort');
  const [load, Re] = useState(false);

  const submitSearch = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log(`searching for "${searchInput}"...`);
    pageNum = 1;
    searchQuery = searchInput;
    beginLoad();
  }
  
  const changeSort = (display: string, query: string) => {
    orderedBy = query;
    orderedByLabel = display;
    //setSortDisplayLabel(display);
    if (!searchInput)
      beginLoad();
    else
      Re(!load);
  }

  const changeInput = (e: any) => {
    searchInput = e.target.value;
    console.log(searchInput);
  }

  return (
    <Form onSubmit={submitSearch} className='slight-bg rounded'>
      <InputGroup>
        <DropdownButton
          variant='info'
          as={InputGroup.Prepend}
          title={orderedByLabel}
        >
          <Dropdown.Item className='text-muted'>Sort results by:</Dropdown.Item>
          <Dropdown.Divider />
          {
            [
              ['Popular', '-score,-created_at'],
              ['New',     '-created_at'],

            ].map(([ display, query ]) => (
              <Dropdown.Item onClick={() => changeSort(display, query)}>{display}</Dropdown.Item>
            ))
          }
        </DropdownButton>
        <Form.Control
          placeholder='Search cards'
          type='string'
          className='slight-bg'
          defaultValue={searchInput}
          onChange={changeInput}
        />
        <div className="input-group-append">
          <button className="btn bg-sdark-red text-white">
            <FontAwesomeIcon icon={faSearch} />
          </button>
        </div>
      </InputGroup>
    </Form>
  );
}

const ListView = ({ user }: ViewProps) => {
  const [cardPage, setCardPage] = useState<CardPage>(null);
  const [start, setStart] = useState(false);

  //var query = useQuery();
  //var page = query.get('page');
  //var pageQuery = page ? `?page=${page}` : '';

  console.log('rendering list');
 
  const beginLoad = () => {
    loaded = false;
    setCardPage(null);
    setStart(!start);
  }
  
  const setPageNum = (n: number) => {
    pageNum = n;
    beginLoad();
  }

  useEffect(() => {
    const getCardPageNum = async () => {
      var searchUrlQuery = searchQuery ? `search=${encodeURIComponent(searchInput)}&` : '';
      var orderedByQuery = orderedBy ? `ordering=${orderedBy}&` : '';

      console.log(`  search query:   "${searchUrlQuery}"`);
      console.log(`  ordering query: "${orderedByQuery}"`);

      try {
        const response = await apiCall(`/api/cards/?${searchUrlQuery}${orderedByQuery}page=${pageNum}`);
        const newCardPage: BingoCardPage = await response.json();

        try {
          newCardPage.results = newCardPage.results.map(card => {
            var tiles = card.tiles.map((tile, index) => {
              tile.hovered = false;
              tile.clicked = false;
              tile.id = index + 1;
              return tile;
            });
            tiles[12].clicked = true;
            card.tiles = tiles;
            return card;
          })
        } catch (err) {}

        setCardPage(newCardPage);
      } catch(err) {
        console.log(err);
      }
      
      //if (cardPage?.detail) {
      //  console.log(`  detail: ${cardPage?.detail}`);
      //}
    }

    getCardPageNum();
  }, [start]);

  const results = (() => {
    if (cardPage && !cardPage.detail) {
      var pages = Math.ceil(cardPage.count / resultsLen);

      console.log(`  pages:   ${pages}`)
      console.log(`  results: ${cardPage.results.length}`)
      console.log(`  count:   ${cardPage.count}`)

      const paginationItems = (() => {
        var current = pageNum,
            last = pages,
            delta = 2,
            left = current - delta,
            right = current + delta + 1,
            range = [],
            rangeWithDots = [],
            l;

        for (let i = 1; i <= last; i++) {
          if (i === 1 || i === last || (i >= left && i < right)) {
            range.push(i);
          }
        }

        const PageItem = ({ index }: { index: number }) => (
          <Pagination.Item
            active={index === pageNum}
            onClick={
              index !== pageNum
                ? () => setPageNum(index)
                : () => {}
            }
          >
            {index}
          </Pagination.Item>
        );
        
        for (let i of range) {
          if (l) {
            if (i - l === 2) {
              rangeWithDots.push(<PageItem index={l + 1}/>);
            } else if (i - l !== 1) {
              rangeWithDots.push(<Pagination.Ellipsis disabled />);
            }
          }
          rangeWithDots.push(<PageItem index={i}/>);
          l = i;
        }

        return rangeWithDots;

      })();

      const cardResults = cardPage.results.map(card => (
        <Col className="p-2">
          <CardInfo card={card} user={user} link/>
        </Col>
      ));

      return (
        <>
          <Row>
            <Col xs={3} className="d-none d-md-block"></Col>
            <Col md={6} className="my-2">
              {
                cardPage.count
                  ? (cardPage.count > resultsLen ? `Page ${pageNum} of ` : '')
                    + `${cardPage.count} `
                    + (searchQuery ? `result` : `bingo card`)
                    + (cardPage.count > 1 ? 's': '')

                  : 'No ' + (searchQuery ? `results for "${searchQuery}"` : 'bingo cards')
              }
            </Col>
            <Col xs={3} className="d-none d-md-block"></Col>
          </Row>
          <Row className="row-cols-1 row-cols-md-2">
            {cardResults}
          </Row> 
          <Pagination className='justify-content-center pt-2'>
            {paginationItems}
          </Pagination>
        </>
      );
    }
  })();
  
  return (
    <div className="p-2">
      <Row className="py-2">
        <Col xs={3} className="d-none d-md-block"></Col>
        <Col className='mt-2'>
          <SearchBar beginLoad={beginLoad}/>
        </Col>
        <Col xs={3} className="d-none d-md-block"></Col>
      </Row>
      {
        results
          ? results 
          : (
              <div className="my-4 text-center">
                {
                  loaded 
                    ? <h1>{cardPage?.detail}</h1> 
                    : <div>
                        <Spinner animation="border" role="status">
                          <span className="sr-only">Loading...</span>
                        </Spinner>
                        <div className="mt-2">
                          <h5>
                          {
                            `Loading page ${pageNum}`
                              + ( searchQuery ? '' : '...')
                          }
                          </h5>
                          {
                            searchQuery
                              ? <h5>{` of search results for "${searchQuery}"...`}</h5>
                              : ''
                          }
                        </div>
                      </div>
                }
              </div>
            )
      }
      <AppNavBar/>
    </div>
  );
}

export default ListView;
