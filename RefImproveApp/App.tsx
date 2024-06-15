import React from 'react';
import {StyleSheet, Text} from 'react-native';

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
  const SubmitBtn = async () => {
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
      <Text style={styles.label}>Field Number</Text>
      <input
        type="text"
        placeholder="Field Number"
        id="fieldNum"
        value={fieldNum}
      />
      <Text style={styles.label}>Home Team</Text>
      <input
        type="text"
        placeholder="Home Team"
        id="homeTeam"
        value={homeTeam}
      />
      <Text style={styles.label}>Away Team</Text>
      <input
        type="text"
        placeholder="Away Team"
        id="awayTeam"
        value={awayTeam}
      />
      <hr />
      <Text style={styles.header4}>
        For Reference: Closest referee is AR 1 and referee by the coaches is AR
        2
      </Text>
      <input
        type="text"
        placeholder="Enter your comments about the Referees here"
        id="refComment"
        value={refComment}
      />
      <input type="button" title="Submit!" onClick={SubmitBtn} />
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
  label: {
    fontSize: 15,
  },
  header4: {
    fontSize: 30,
  },
});

export default App;
