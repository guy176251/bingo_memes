import { useLocation } from "react-router-dom";
import { Helmet } from "react-helmet";

import CardList from "../components/cardlist";
import { Header } from "../components/snippets";
import debugLog from "../debug";
import { CardListSidebar } from "../components/cardlist";

//const headerPadding = 'rounded text-center sdark-fg p-4';

const SearchView = () => {
    const urlParams = new URLSearchParams(useLocation().search);
    const searchQuery = urlParams.get("q") || "";
    const cardQuery = { search: encodeURIComponent(searchQuery) };

    debugLog({ SEARCHVIEW: 1, searchQuery });
    return (
        <>
            <Helmet>
                <title>Search</title>
            </Helmet>
            <CardListSidebar
                query={cardQuery}
                infoCol={
                    <div className="text-center">
                        <h3>Search results for "{searchQuery}"</h3>
                    </div>
                }
            />
        </>
    );
};

export default SearchView;
