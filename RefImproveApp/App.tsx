import React from 'react';
import {StyleSheet} from 'react-native';

interface RefereeObj {
  FIELDNUM: string;
  HOMETEAM: string;
  AWAYTEAM: string;
  REFCOMMENT: string;
}

const App = (
  fieldNum: string,
  homeTeam: string,
  awayTeam: string,
  refComment: string,
) => {
  let isHidden = false;
  const submitBtn = async () => {
    const ref: RefereeObj = {
      FIELDNUM: fieldNum,
      HOMETEAM: homeTeam,
      AWAYTEAM: awayTeam,
      REFCOMMENT: refComment,
    };
    const res: Response = await fetch(
      'http://127.0.0.1:5000//api/referee-improvement',
    );
    if (res.ok) {
      isHidden = true;
    }
  };

  return (
    <div style={isHidden ? styles.hidden : styles.visible}>
      <text>Field Number</text>
      <input
        type="text"
        placeholder="Field Number"
        id="fieldNum"
        value={fieldNum}
      />
      <text>Home Team</text>
      <input
        type="text"
        placeholder="Home Team"
        id="homeTeam"
        value={homeTeam}
      />
      <text>Away Team</text>
      <input
        type="text"
        placeholder="Away Team"
        id="awayTeam"
        value={awayTeam}
      />
      <hr />
      <text>
        For Reference: Closest referee is AR 1 and referee by the coaches is AR
        2
      </text>
      <input
        type="text"
        placeholder="Enter your comments about the Referees here"
        id="refComment"
        value={refComment}
      />
      <input type="button" title="Submit!" onClick={submitBtn} />
    </div>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  text: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  hidden: {
    display: 'none',
  },
  visible: {
    display: 'flex',
  },
});

export default App;
