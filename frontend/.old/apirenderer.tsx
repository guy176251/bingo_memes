import React, { useEffect, useState } from 'react';
import Spinner from 'react-bootstrap/Spinner';
import apiCall from './apicaller';

interface RespState {
    data: any | null;
    statusCode: number;
}

const getData = async (
    url: string,
    setResp: (c: RespState) => void,
    setFound: ((b: boolean) => void) | undefined,
) => {

    setResp({ data: null, statusCode: 200 });
    
    if (setFound)
        setFound(false);

    var resp = await apiCall(url);
    var data: any | null;

    try {
        data = await resp.json();
    } catch {
        data = null;
    }

    if (data && resp.status < 300 && setFound)
        setFound(true);

    setResp({ data: data, statusCode: resp.status });
}

interface MainViewProps {
    data: any;
}

interface ApiRendererProps {
    url: string;
    loadingMessage?: string;
    element: React.FunctionComponent<MainViewProps>;
    setFound?: (b: boolean) => void;
}

const ApiRenderer = ({ url, loadingMessage, element, setFound }: ApiRendererProps) => {
    const [ resp, setResp ] = useState<RespState>({ data: null, statusCode: 200 });
    const Element = element;
    const { data, statusCode } = resp;
     
    useEffect(() => {
        getData(url, setResp, setFound);
    }, [url]);

    const respStatus = (
         (data?.detail || statusCode >= 300)

            ? <div className='text-sdark-red text-center my-4'>
                    <h3>
                        {`Error ${statusCode}` + (data?.detail ? `: ${data.detail}` : '')}
                    </h3>
                </div>

            : <div className='text-center mt-4'>
                    <Spinner animation="border" role="status">
                        <span className="sr-only">Loading...</span>
                    </Spinner>
                    {
                        loadingMessage &&
                            <div className="mt-2">
                                {loadingMessage}
                            </div>
                    }
                </div>
    );
    
    const pageContent = (
        data && (!data.detail && statusCode < 300)
            ? <Element data={data}/>
            : respStatus
    );
 
    //console.log(`RENDERER\n\n    url: ${url}\n    data: ${(data ? '\n        ' + Object.entries(data).map(([ key, value ]) => `${key}: ${value}`).join('\n        ') : 'None')}`);
    return (
        <>{pageContent}</>
    );
}

export default ApiRenderer;
