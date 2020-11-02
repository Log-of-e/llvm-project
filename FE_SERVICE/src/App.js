import React from "react";
import "./styles.css";
import 'bootstrap/dist/css/bootstrap.min.css';

import {Fileview} from "./Fileview"


export default function App() {
  // React.useEffect(() => {
  //   getFileInfo().then((fils) => console.log({ fils }));
  // });
  return (
    <div className="App">
      <h1>  View File Analysis</h1>
      <h2> </h2>
        <div></div>
        <Fileview></Fileview>
    </div>
  );
}

// async function getFileInfo() {
//   const fileList = await fetch("http://localhost:8080/file_list");
//   const fileInfo = await fetch("http://localhost:8080/process/a75");
//   return { fileList, fileInfo };
// }
