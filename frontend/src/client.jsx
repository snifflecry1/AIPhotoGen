import { useState } from "react";
import "./client.css"; // Import CSS file

const Client = () => {
  const [entries, setEntries] = useState([]);
  const [newEntry, setNewEntry] = useState("");

  const addEntry = () => {
    if (newEntry.trim() === "") return;
    const newDiaryEntry = {
      id: entries.length + 1,
      content: newEntry,
      date: new Date(),
    };
    setEntries([newDiaryEntry, ...entries]);
    setNewEntry("");
  };

  return (
    <div className="diary-container">
      <textarea
        className="diary-textarea"
        value={newEntry}
        onChange={(e) => setNewEntry(e.target.value)}
        placeholder="Write your stupid extra shitty diary entry..."
        rows="3"
      />
      <button className="add-entry-btn" onClick={addEntry}>
        Add Entry
      </button>
      <ul className="diary-list">
        {entries.map((entry) => (
          <li key={entry.id} className="diary-entry">
            <strong>{entry.date.toDateString()}</strong>
            <p>{entry.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Client;
