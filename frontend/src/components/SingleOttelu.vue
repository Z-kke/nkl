<template>
  <v-container grid-list-md>
    <v-layout row wrap align-center>
      <v-flex xm12>
        <match v-if="data_ready" :matchData="data"></match>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xm6>
        <v-card color="secondary">
          <round v-if="data_ready" :matchData="data" roundNumber="1" teamSide="home"></round>
        </v-card>
      </v-flex>
      <v-flex xm6>
        <v-card color="secondary">
          <round v-if="data_ready" :matchData="data" roundNumber="1" teamSide="away"></round>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xm6>
        <v-card color="secondary">
          <round v-if="data_ready" :matchData="data" roundNumber="2" teamSide="home"></round>
        </v-card>
      </v-flex>
      <v-flex xm6>
        <v-card color="secondary">
          <round v-if="data_ready" :matchData="data" roundNumber="2" teamSide="away"></round>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex class="text-xs-center" xm12>
        <v-btn v-if="data_ready && away_captain" v-on:click="validateClick" x-large color="error">vahvista</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Round from '@/components/SingleRound';
import Match from '@/components/MatchData';

export default {
    name: 'ottelu',
    components: {
        Round,
        Match
    },
    data: function() {
        return {
          data: {},
          data_ready: false,
          away_captain: false,
        };
    },
    methods: {
      getData: function() {
        this.$http
        .get(
            'api/matches/' +
                this.$route.fullPath.substr(
                    this.$route.fullPath.lastIndexOf('/') + 1
                )
        )
        .then(function(data) {
          this.data = data
          this.data_ready = true
          if(!data.body.is_validated && localStorage.role_id == 1 && localStorage.team_id == this.data.body.away_team.id) {
            this.away_captain = true
          }
        })
      },
      validateClick: function() {
        let post_url = 'api/matches/'+this.data.body.id
        let post_data = {"is_validated": true}

        if (confirm('Oletko tyytyväinen ottelun tuloksiin?')) {
          this.$http.patch(post_url, post_data, {
            headers: {
              'X-CSRFToken': this.getCookie('csrftoken')
            },
            'withCredentials': true,
          }).then(function(response){
            this.data.is_validated = true
            window.location.reload()
            }).catch(function(response) {
              if (response.status == 403) {
                this.$http
                  .get('api/csrf', {'withCredentials': true})
                  .then(function(response) {
                      if (response.status === 200) {
                          this.$http.patch(post_url, post_data, {
                          headers: {
                            'X-CSRFToken': this.getCookie('csrftoken')
                          },
                          'withCredentials': true,
                          })
                      }
                  });
              }
          })
        }
      }
    },
    created: function() {
      this.getData()
    },
};
</script>

<style>
</style>
