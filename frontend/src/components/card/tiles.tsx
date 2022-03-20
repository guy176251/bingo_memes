import { Components } from "types/apiclient";

type NavVariant = "dark" | "light" | undefined;
type NavExpand = boolean | "lg" | "sm" | "md" | "xl" | "xxl" | undefined;
type SolutionState = number[] | null;

interface Props {
    card: Components.Schemas.CardDetailSchema;
}

interface Tile {
    text: string;
    clicked: boolean;
    hovered: boolean;
    index: number;
}

const solutionArrays = (() => {
    // Bingo card is 5 x 5, so can use the same length array
    // for all the dimensions.
    const side = Array(5).fill(0);

    const edge = side.map((_, i) => i);
    const diag1 = side.map((_, i) => i * 4 + 4);
    const diag2 = side.map((_, i) => i * 6);
    const vert = edge.map((n) => side.map((_, i) => i * 5 + n));
    const horiz = edge.map((n) => side.map((_, i) => i + 5 * n));

    return [...vert, ...horiz, diag1, diag2];
})();

function hasBingo(tiles: Tile[]): SolutionState {
    if (tiles.length !== 25) {
        return null;
    }
    for (const solution of solutionArrays) {
        if (solution.some((index) => !tiles[index].clicked)) {
            continue;
        } else {
            return solution;
        }
    }
    return null;
}

function getTilesFromCard(card: Components.Schemas.CardDetailSchema): Tile[] {
    const collator = new Intl.Collator("en", { numeric: true });
    return Object.entries(card)
        .filter(([field, _]) => field.startsWith("tile_"))
        .sort(([field1, _], [field2, __]) => collator.compare(field1, field2))
        .map(([_, text], index) => ({
            hovered: false,
            clicked: index === 12,
            index: index + 1,
            text,
        }));
}

const styles = {
    gutter: "g-3",
    subGutter: "g-2",
    tilePadding: "py-2 pe-3",
    tileLook: "bg-light rounded",
    tileIndexLook: "text-center border-end h-100",
    tileClickedLook: "bg-secondary text-white rounded",
    navBg: "dark",
    navVariant: "dark" as NavVariant,
    navLook: "rounded",
    navExpand: "lg" as NavExpand,
    navPadding: "px-2",
    indicatorLook: "text-center p-2",
    searchPadding: "mx-3",
};

export default function CardTileComponentNew({ card }: Props) {
    /*
    const [solution, setSolution] = useState<SolutionState>(null);
    const [tiles, setTiles] = useState<Tile[]>(() => getTilesFromCard(card));
    const [search, setSearch] = useState("");

    const clickTile = (index: number) => {
        const tilesCopy = [...tiles];
        tilesCopy[index].clicked = !tilesCopy[index].clicked;
        setTiles(tilesCopy);
        setSolution(hasBingo(tilesCopy));
    };
    const resetTiles = () => {
        const tilesCopy = [...tiles];
        setTiles(
            tilesCopy.map((tile) => {
                tile.clicked = tile.index === 13;
                return tile;
            })
        );
        setSolution(null);
    };
    const searchedTiles: Tile[] = search
        ? tiles.filter((tile) => tile.text.toLowerCase().includes(search.toLowerCase()))
        : tiles;
        */
    /*
    const {
        tiles,
        search,
        setSearch,
        searchedTiles,
        clickTile,
        solution,
        resetTiles,
        setTilesFromCard,
    } = useTiles();

    useEffect(() => {
        setTilesFromCard(card);
    }, []);

        */
    return <></>;
}
