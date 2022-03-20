//import { abort } from "process";

const DEBUG = true;
const debugLog = (debugObject: any) => {
    if (DEBUG) {
        /*
    const logBody = Object.entries(props)
      .map(([key, value]) => `${key}: ${value}`)
      .join("\n  ");

    console.log(`{\n  ${logBody}\n}`);
    */
        try {
            console.log(JSON.stringify(debugObject, null, 4));
        } catch (err) {
            console.log(err);
        }
    }
    //DEBUG && console.log(props);
};

export default debugLog;
