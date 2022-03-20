import { createContext, useContext, useState } from "react";
import { Components } from "types/apiclient";

type SolutionState = number[] | null;
type BingoCard = Components.Schemas.CardDetailSchema;

interface Tile {
    text: string;
    clicked: boolean;
    hovered: boolean;
    index: number;
}

interface TileData {
    tiles: Tile[];
    setTiles: (t: Tile[]) => void;
    solution: SolutionState;
    setSolution: (s: SolutionState) => void;
    search: string;
    setSearch: (s: string) => void;
    searchedTiles: Tile[];
    clickTile: (index: number) => void;
    resetTiles: () => void;
    setTilesFromCard: (c: BingoCard) => void;
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

function useTileData(): TileData {
    const [solution, setSolution] = useState<SolutionState>(null);
    const [tiles, setTiles] = useState<Tile[]>([]);
    const [search, setSearch] = useState("");

    const searchedTiles: Tile[] = search
        ? tiles.filter((tile) => tile.text.toLowerCase().includes(search.toLowerCase()))
        : tiles;

    return {
        tiles,
        solution,
        search,
        searchedTiles,
        setTiles,
        setSolution,
        setSearch,
        clickTile(index: number) {
            const tilesCopy = [...tiles];
            tilesCopy[index].clicked = !tilesCopy[index].clicked;
            setTiles(tilesCopy);
            setSolution(hasBingo(tilesCopy));
        },
        resetTiles() {
            const tilesCopy = [...tiles];
            setTiles(
                tilesCopy.map((tile) => {
                    tile.clicked = tile.index === 13;
                    return tile;
                })
            );
            setSolution(null);
        },
        setTilesFromCard(card: BingoCard) {
            const collator = new Intl.Collator("en", { numeric: true });
            const newTiles = Object.entries(card)
                .filter(([field, _]) => field.startsWith("tile_"))
                .sort(([field1, _], [field2, __]) => collator.compare(field1, field2))
                .map(([_, text], index) => ({
                    hovered: false,
                    clicked: index === 12,
                    index: index + 1,
                    text,
                }));
            setTiles(newTiles);
        },
    };
}

const TileContext = createContext<TileData>({
    tiles: [],
    setTiles: (t: Tile[]) => {},
    solution: null,
    setSolution: (s: SolutionState) => {},
    search: "",
    setSearch: (s: string) => {},
    searchedTiles: [],
    clickTile: (index: number) => {},
    resetTiles: () => {},
    setTilesFromCard: (c: Components.Schemas.CardDetailSchema) => {},
});

export function ProvideTiles({ children }: { children: any }) {
    const tileData = useTileData();
    return <TileContext.Provider value={tileData}>{children}</TileContext.Provider>;
}

export function useTiles() {
    return useContext(TileContext);
}
