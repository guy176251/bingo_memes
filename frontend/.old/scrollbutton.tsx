import 'react-tiny-fab/dist/styles.css';
import { Fab } from 'react-tiny-fab';
//import { FaArrowUp, FaPlus } from 'react-icons/fa'

interface ButtonProps {
  show: boolean;
}

export default function ScrollButton({ show = true }: ButtonProps) {
  var scrollToTop = () => window.scrollTo({
    top: 0,
    behavior: "smooth"
  });

  return (
    <div className={show ? 'd-md-none' : 'd-none'}>
      <Fab
        icon='⮝'
        mainButtonStyles={{ backgroundColor: 'crimson' }}
        onClick={scrollToTop}
      >
      </Fab>
    </div>
  );
}
