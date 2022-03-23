import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";

const styles = {
    paragraph: "lead text-muted",
    title: "fw-light",
};

export default function AboutView() {
    return (
        <div className="text-center my-5">
            <Row className="g-5">
                <Col xs={12}>
                    <h1 className={styles.title}>About Bingo Memes</h1>
                    <p className={styles.paragraph}>
                        Bingo Memes is a website that was created to share bingo meme templates.{" "}
                    </p>
                    <a
                        className="btn text-white bg-sdark-orange rounded-pill mt-3 px-3"
                        href="https://github.com/guy176251/bingo_memes"
                    >
                        Link to Github Repo
                    </a>
                    <a
                        className="btn text-white bg-sdark-blue rounded-pill mt-3 px-3 ms-2"
                        href="/"
                    >
                        Homepage
                    </a>
                </Col>
                {/*
                <Col xs={12}>
                    <h3 className={styles.title}>What is a bingo meme?</h3>
                    <p className={styles.paragraph}>
                        Imagine a traditional bingo card, but instead of arbitrary letters and numbers in the grid
                        squares, replace them with various facts or events about a subject.  
                    </p>
                </Col>
                */}
            </Row>
        </div>
    );
}
