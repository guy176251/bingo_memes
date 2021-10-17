/*
const SearchBarr = () => {
    const [ searchInput, setSearchInput ] = useState('');
    const [ showDropdown, setShowDropdown ] = useState(false);
    const [ searchRoute, setSearchRoute ] = useState('');
    const hist = useHistory();

    useEffect(() => {
        if (searchRoute) {
            hist.push(searchRoute);
            setSearchRoute('');
        }
    }, [hist, searchRoute]);
 
    const toggleDropdown = (state: boolean = false) => {
        if (searchInput.length > 0 && !showDropdown)
            return true;
        return state;
    };

    const searchLog = (label: string) => {
        let spacer = '\n        ';
        console.log(`${label}:${spacer}${
            Object.entries({
                searchInput: searchInput,
                searchRoute: searchRoute,
                showDropdown: showDropdown,
            }).map(([ text, value ]) => (
                `${text}: "${value}"`
            )).join(spacer)
        }`);
    }

    searchLog('SEARCHBAR DRAW');
    
    return (
        <Dropdown
            show={showDropdown}
            onToggle={() => {
                searchLog('SEARCHBAR ONTOGGLE');
                setShowDropdown(toggleDropdown());
            }}
            onSelect={(eventKey) => {
                if (eventKey) {
                    setSearchInput('');
                    setShowDropdown(false);
                    setSearchRoute(`${eventKey}${encodeURIComponent(searchInput)}`);
                    console.log(`SEARCHROUTE: ${searchRoute}`);
                }
            }}
        >
            <Dropdown.Toggle as={DropdownContainer} id='search-bar'>
                <div className="input-group">
                    <div
                        className="input-group-prepend"
                        style={{ cursor: 'pointer' }}
                    >
                        <span className="input-group-text">
                            <FaIcon icon={faSearch}/>
                        </span>
                    </div>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Search"
                        value={searchInput}
                        onChange={e => {
                            let inputText = e.target.value;
                            let showDropdown = false;
                            
                            if (inputText.length > 0) {
                                showDropdown = true;
                            }

                            setSearchInput(inputText);
                            setShowDropdown(showDropdown);
                        }}
                    />
                </div>
            </Dropdown.Toggle>

            <Dropdown.Menu className='w-100 mt-2 slight-bg'>
                {Object.entries({ 'cards': '/search?q=' }).map(([ label, url ]) => (
                    <Dropdown.Item className='slight-bg' eventKey={url}>
                        Search for "{label}": {searchInput}
                    </Dropdown.Item>
                ))}
            </Dropdown.Menu>
        </Dropdown>
    );
};
*/
